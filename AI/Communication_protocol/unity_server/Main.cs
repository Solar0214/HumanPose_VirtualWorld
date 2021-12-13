using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Main : MonoBehaviour
{
    #region sigleton
    private static Main _instance;
    public static Main Getsingleton
    {
        get
        {
            if (_instance == null)
            {
                _instance = FindObjectOfType(typeof(Main)) as Main;
                if (_instance == null)
                {
                    _instance = new GameObject("Main").AddComponent<Main>();
                    DontDestroyOnLoad(_instance.gameObject);
                }
            }
            return _instance;
        }
    }
    #endregion
    public Player OwnPlayer;
    private Dictionary<uint, Player> Dic_Players = new Dictionary<uint, Player>();

    private void Start()
    {
        NetSocketManager.Getsingleton.Init();


        if (OwnPlayer != null)
            Dic_Players[OwnPlayer.UserId] = OwnPlayer;

        OwnPlayer.InitPlayer(PlayerKind.Player);
    }


    public void NetReceived_MovePosPlayer(ByteData packet)
    {
        uint userid = packet.Getuint();

        if(Dic_Players.ContainsKey(userid))
        {
            Dic_Players[userid].ReceivedMovePlayerData(packet);
        }
        else
        {
            //생성
            GameObject newPlayerOJ = Instantiate(Resources.Load("Player") as GameObject);

            if(newPlayerOJ!=null)
            {
                Player p = newPlayerOJ.GetComponent<Player>();
                p.UserId = userid;
                p.InitPlayer(PlayerKind.Network);
                p.ForceNetPlayerPos(packet);
                Dic_Players[userid] = p;
            }
        }
    }




    private void OnApplicationQuit()
    {

        NetSocketManager.Getsingleton.Disconnect();
    }
}
