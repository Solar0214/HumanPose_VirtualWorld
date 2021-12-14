using System;
using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Runtime.InteropServices;

public class Receiver : MonoBehaviour
{
    private UdpClient m_Receiver;
    public string m_Ip = "127.0.0.1";
    public int m_Port = 9505;
    public Packet m_ReceivePacket = new Packet();
    private IPEndPoint m_IpEndPoint;

    void Start()
    {
        InitReceiver();
    }

    void Update()
    {
        Receive();
    }

    void OnApplicationQuit()
    {
        CloseReceiver();
    }

    void InitReceiver()
    {
        m_Receiver = new UdpClient();
        m_Receiver.ExclusiveAddressUse = false;
        IPEndPoint localIpEndPoint = new IPEndPoint(IPAddress.Any, m_Port);
        m_Receiver.Client.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReuseAddress, true);
        m_Receiver.ExclusiveAddressUse = false;
        m_Receiver.Client.Bind(localIpEndPoint);

        IPAddress multicastIPAddress = IPAddress.Parse(m_Ip);
        m_Receiver.JoinMulticastGroup(multicastIPAddress);

        m_IpEndPoint = new IPEndPoint(IPAddress.Any, m_Port);
    }

    void Receive()
    {
        if (m_Receiver.Available != 0)
        {
            byte[] packet = new byte[4096];

            try
            {
                packet = m_Receiver.Receive(ref m_IpEndPoint);
            }

            catch (Exception ex)
            {
                Debug.Log(ex.ToString());
                return;
            }

            m_ReceivePacket = ByteArrayToStruct<Packet>(packet);
            DoReceivePacket(); // 받은 값 처리
        }
    }

    void DoReceivePacket()
    {
        Debug.LogFormat($"m_IntArray[0] = {m_ReceivePacket.m_IntArray[0]} " +
            $"m_IntArray[1] = {m_ReceivePacket.m_IntArray[1] } " +
            $"FloatlVariable = {m_ReceivePacket.m_FloatlVariable} " +
            $"StringlVariable = {m_ReceivePacket.m_StringlVariable}" +
            $"BoolVariable = {m_ReceivePacket.m_BoolVariable} " +
            $"IntlVariable = {m_ReceivePacket.m_IntVariable} ");
        //출력: m_IntArray[0] = 7 m_IntArray[1] = 47 FloatlVariable = 2020 StringlVariable = Coder ZeroBoolVariable = True IntlVariable = 13 
    }

    void CloseReceiver()
    {
        if (m_Receiver != null)
        {
            m_Receiver.Close();
            m_Receiver = null;
        }
    }

    T ByteArrayToStruct<T>(byte[] buffer) where T : struct
    {
        int size = Marshal.SizeOf(typeof(T));
        if (size > buffer.Length)
        {
            throw new Exception();
        }

        IntPtr ptr = Marshal.AllocHGlobal(size);
        Marshal.Copy(buffer, 0, ptr, size);
        T obj = (T)Marshal.PtrToStructure(ptr, typeof(T));
        Marshal.FreeHGlobal(ptr);
        return obj;
    }
}



/*
 https://coderzero.tistory.com/entry/%EC%9C%A0%EB%8B%88%ED%8B%B0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-Multicast-Sender-Multicast-Receiver-%EA%B5%AC%EC%A1%B0%EC%B2%B4-%EC%A0%84%EC%86%A1-UdpClient?category=400220
 */