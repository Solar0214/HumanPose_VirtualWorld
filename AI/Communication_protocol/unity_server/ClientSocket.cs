using System;
using System.Collections;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using UnityEngine;
public enum NetKind { Connect, Disconnect, Move, }

public delegate void DelSocketReceive(byte[] packet);

public class ClientSocket
{
    private Socket NetSocket;
    EndPoint severEndPoint;

    private DelSocketReceive CallbackReceiveData;

    public ClientSocket(DelSocketReceive _CallbackReceiveData)
    {
        CallbackReceiveData = _CallbackReceiveData;

    }

    public void ConnectSocket()
    {

        NetSocket = new Socket(AddressFamily.InterNetwork, SocketType.Dgram, ProtocolType.Udp);

        severEndPoint = new IPEndPoint(IPAddress.Parse("127.0.0.1"), 9505);

        byte[] msg = new byte[4];
        NetKind netknd = NetKind.Connect;
        msg[0] = (byte)netknd;

        NetSocket.SendTo(msg, severEndPoint);


        byte[] buffer = new byte[1024];
        NetSocket.BeginReceiveFrom(buffer, 0, buffer.Length, SocketFlags.None, ref severEndPoint, CallbackRecieveFrom, buffer);
    }


    private void CallbackRecieveFrom(IAsyncResult result)
    {
        byte[] receiveData = new byte[1024];
        receiveData = (byte[])result.AsyncState;

        if (CallbackReceiveData != null)
            CallbackReceiveData(receiveData);

        byte[] byteData = new byte[1024];
        NetSocket.BeginReceiveFrom(byteData, 0, byteData.Length, SocketFlags.None, ref severEndPoint, CallbackRecieveFrom, byteData);
    }



    public void SendPacketData(byte[] data)
    {
        NetSocket.SendTo(data, severEndPoint);
    }
}
