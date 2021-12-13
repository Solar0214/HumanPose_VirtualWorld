using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NetSocketManager : MonoBehaviour
{

    #region sigleton
    private static NetSocketManager _instance;
    public static NetSocketManager Getsingleton
    {
        get
        {
            if (_instance == null)
            {
                _instance = FindObjectOfType(typeof(NetSocketManager)) as NetSocketManager;
                if (_instance == null)
                {
                    _instance = new GameObject("NetSocketManager").AddComponent<NetSocketManager>();
                    DontDestroyOnLoad(_instance.gameObject);
                }
            }
            return _instance;
        }
    }
    #endregion

    private ClientSocket NetSocket;
    public void Init()
    {
        NetSocket = new ClientSocket(RecievedPacketData);
        NetSocket.ConnectSocket();
    }


    Queue<ByteData> Que_Packet = new Queue<ByteData>();
    void RecievedPacketData(byte[] packet)
    {
        ByteData data = new ByteData(packet);
        Que_Packet.Enqueue(data);
    }

    void ProcessReceivedPacket()
    {
        if(Que_Packet.Count > 0)
        {
            ByteData receivedData = Que_Packet.Dequeue();
            NetKind knd = (NetKind)receivedData.Getbyte();
            Debug.Log("ReceivedPacket : " + knd);
            switch (knd)
            {
                case NetKind.Connect:
                    break;
                case NetKind.Disconnect:
                    break;
                case NetKind.Move:
                    Main.Getsingleton.NetReceived_MovePosPlayer(receivedData);
                    break;
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        ProcessReceivedPacket();
    }







    public void SendData(ByteData packet)
    {
        if (NetSocket == null) return;

        NetSocket.SendPacketData(packet.data);
    }


    public void Disconnect()
    {
        ByteData data = new ByteData(2, 0);
        data.InPutByte((byte)NetKind.Disconnect);
        SendData(data);
    }

}
