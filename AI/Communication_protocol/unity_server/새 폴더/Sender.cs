using System;
using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Runtime.InteropServices;

public class Sender : MonoBehaviour
{
    private UdpClient m_Sender;
    public string m_Ip = "224.0.1.0";
    public int m_Port = 50001;
    public Packet m_SendPacket = new Packet();
    private IPEndPoint m_IpEndPoint;

    void Start()
    {
        InitSender();
    }

    void Update()
    {
        Send();
    }

    void OnApplicationQuit()
    {
        CloseSender();
    }

    void InitSender()
    {
        m_Sender = new UdpClient();
        IPAddress ipAddress = IPAddress.Parse(m_Ip);
        m_Sender.JoinMulticastGroup(ipAddress);
        m_IpEndPoint = new IPEndPoint(ipAddress, m_Port);

        // SendPacket에 배열이 있으면 선언 해 주어야 함.
        m_SendPacket.m_IntArray = new int[2];
    }

    void Send()
    {
        try
        {
            SetSendPacket();

            byte[] sendPacket = StructToByteArray(m_SendPacket);
            m_Sender.Send(sendPacket, sendPacket.Length, m_IpEndPoint);
        }

        catch (Exception ex)
        {
            Debug.Log(ex.ToString());
            return;
        }
    }

    void SetSendPacket()
    {
        m_SendPacket.m_BoolVariable = true;
        m_SendPacket.m_IntVariable = 13;
        m_SendPacket.m_IntArray[0] = 7;
        m_SendPacket.m_IntArray[1] = 47;
        m_SendPacket.m_FloatlVariable = 2020;
        m_SendPacket.m_StringlVariable = "Coder Zero";
    }

    void CloseSender()
    {
        if (m_Sender != null)
        {
            m_Sender.Close();
            m_Sender = null;
        }
    }

    byte[] StructToByteArray(object obj)
    {
        int size = Marshal.SizeOf(obj);
        byte[] arr = new byte[size];
        IntPtr ptr = Marshal.AllocHGlobal(size);

        Marshal.StructureToPtr(obj, ptr, true);
        Marshal.Copy(ptr, arr, 0, size);
        Marshal.FreeHGlobal(ptr);
        return arr;
    }
}