using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public enum PlayerKind { Player,Network, }
public class Player : MonoBehaviour
{
    private int DirectionX;
    private int DirectionZ;
    private float speed = 5f;
    private Transform Tr;
    public PlayerKind PlayerKnd = PlayerKind.Player;
    public uint UserId;
    void Start()
    {
       

        UserId = (uint)Random.Range(1, 50000);
    }

    public void InitPlayer(PlayerKind pknd)
    {
        Tr = this.transform;

        PlayerKnd = pknd;

        if(PlayerKnd == PlayerKind.Player)
        {
            CoSendPosPlayer = StartCoroutine(Co_SendPosPlayer());
        }
    }

    // Update is called once per frame
    void Update()
    {

        InputProcess();



    }

    int count = 0;
    void InputProcess()
    {
        if (PlayerKnd == PlayerKind.Network) return;


       

        if (Input.GetKey(KeyCode.A))
        {
            DirectionX = -1;
        }
        else if (Input.GetKeyUp(KeyCode.A))
        {
            DirectionX = 0;

        }

        if (Input.GetKey(KeyCode.D))
        {
            DirectionX = 1;

        }
        else if (Input.GetKeyUp(KeyCode.D))
        {
            DirectionX = 0;

        }

        if (Input.GetKey(KeyCode.S))
        {
            DirectionZ = -1;
        }
        else if (Input.GetKeyUp(KeyCode.S))
        {
            DirectionZ = 0;

        }

        if (Input.GetKey(KeyCode.W))
        {
            DirectionZ = 1;

        }
        else if (Input.GetKeyUp(KeyCode.W))
        {
            DirectionZ = 0;
        }
    }


    private void FixedUpdate()
    {

       

        MovePlayerProcess();

        NetworkMovePlayerProcess();

    }


    void MovePlayerProcess()
    {
        if (PlayerKnd == PlayerKind.Network) return;

        Tr.Translate(new Vector3(DirectionX, 0f, DirectionZ) * speed * Time.deltaTime);
    }


    Coroutine CoSendPosPlayer = null;
    IEnumerator Co_SendPosPlayer()
    {
        yield return new WaitForSeconds(0.1f);

        SendPosPlayerData();

        CoSendPosPlayer = StartCoroutine(Co_SendPosPlayer());
    }

    void SendPosPlayerData()
    {
        ByteData sendData = new ByteData(64,0);

        sendData.InPutByte((byte)NetKind.Move);
        sendData.InPutByte(UserId);
        //현재위치
        sendData.InPutByte(Tr.position);
        //가는방향
        sendData.InPutByte(DirectionX);
        sendData.InPutByte(DirectionZ);

        //속도?

        NetSocketManager.Getsingleton.SendData(sendData);

    }



    Vector3 NetPlayerPos = new Vector3();
    Vector3 NetPlayerDir = new Vector3();
    public void ReceivedMovePlayerData(ByteData data)
    {
        NetPlayerPos = data.GetVector3();
        int dirX = data.Getint();
        int dirZ = data.Getint();
        NetPlayerDir = new Vector3(dirX, 0, dirZ);

        Debug.Log("NetPlayerDir : " + NetPlayerDir + " / " +NetPlayerDir.magnitude);
    }
    public void ForceNetPlayerPos(ByteData data)
    {
        NetPlayerPos = data.GetVector3();
        int dirX = data.Getint();
        int dirZ = data.Getint();
        NetPlayerDir = new Vector3(dirX, 0, dirZ);

        Tr.position = NetPlayerPos;
    }


    void NetworkMovePlayerProcess()
    {
        if (PlayerKnd == PlayerKind.Player) return;

        //Tr.position = Vector3.Lerp(Tr.position,NetPlayerPos,Time.deltaTime*10f);

        //Tr.Translate(NetPlayerDir * speed * Time.deltaTime);

        if (NetPlayerDir.magnitude > 0)
            Tr.position = Tr.position + (NetPlayerDir * speed * Time.deltaTime);
        else
            Tr.position = Vector3.Lerp(Tr.position, NetPlayerPos, Time.deltaTime * 10f);
    }

}
