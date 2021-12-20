using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using System;
using System.Net;
using System.Net.Sockets;
using System.Runtime.InteropServices;
using System.Text;


public class Receiver : MonoBehaviour
{
    private UdpClient m_Receiver;
    public int m_Port = 9505;
    public Packet m_ReceivePacket = new Packet();
    private IPEndPoint m_IpEndPoint;
    public Animator animator;
    public Transform[] humanJoint = new Transform[NUM_JOINT];
    private Vector3[] posData = new Vector3[33];
    public const int NUM_JOINT = 16;
    public Transform now;

    void Start()
    {
        InitReceiver();
        Debug.Log("Start");

    }


    void Update()
    {
        Receive();
        Debug.Log("while - Start");
        animator = GetComponent<Animator>();
        if (animator)
        {
            //아바타의 bone transforms을 가져옴
            humanJoint[0] = animator.GetBoneTransform(HumanBodyBones.RightFoot);
            humanJoint[1] = animator.GetBoneTransform(HumanBodyBones.RightLowerLeg);
            humanJoint[2] = animator.GetBoneTransform(HumanBodyBones.RightUpperLeg);
            humanJoint[3] = animator.GetBoneTransform(HumanBodyBones.LeftUpperLeg);
            humanJoint[4] = animator.GetBoneTransform(HumanBodyBones.LeftLowerLeg);
            humanJoint[5] = animator.GetBoneTransform(HumanBodyBones.LeftFoot);
            humanJoint[6] = animator.GetBoneTransform(HumanBodyBones.Hips);
            humanJoint[7] = animator.GetBoneTransform(HumanBodyBones.UpperChest);
            humanJoint[8] = animator.GetBoneTransform(HumanBodyBones.Neck);
            humanJoint[9] = animator.GetBoneTransform(HumanBodyBones.Head);
            humanJoint[10] = animator.GetBoneTransform(HumanBodyBones.RightHand);
            humanJoint[11] = animator.GetBoneTransform(HumanBodyBones.RightLowerArm);
            humanJoint[12] = animator.GetBoneTransform(HumanBodyBones.RightUpperArm);
            humanJoint[13] = animator.GetBoneTransform(HumanBodyBones.LeftUpperArm);
            humanJoint[14] = animator.GetBoneTransform(HumanBodyBones.LeftLowerArm);
            humanJoint[15] = animator.GetBoneTransform(HumanBodyBones.LeftHand);
        }
    }

    void OnApplicationQuit()
    {
        CloseReceiver();
    }

    void InitReceiver()
    {
        m_Receiver = new UdpClient();

        m_IpEndPoint = new IPEndPoint(IPAddress.Any, m_Port);

        m_Receiver.Client.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReuseAddress, true);
        m_Receiver.ExclusiveAddressUse = false;
        m_Receiver.Client.Bind(m_IpEndPoint);
    }

    void Receive()
    {
        Debug.Log("receive Start");
        if (m_Receiver.Available != 0)
        {
            byte[] packet = new byte[12288];
            

            try
            {
                Debug.Log(m_Receiver.Receive(ref m_IpEndPoint));
                packet = m_Receiver.Receive(ref m_IpEndPoint);
                string tmp = Encoding.ASCII.GetString(packet);
                Debug.Log("3");
                tmp = tmp.Replace("\'", "\"");
                //Debug.Log(tmp);
                processJsonData(tmp);
                Debug.Log("4");
            }

            catch (Exception ex)
            {
                Debug.Log(ex.ToString());
                return;
            }

            
            m_ReceivePacket = ByteArrayToStruct<Packet>(packet);
            DoReceivePacket(); // 받은 값 처리
            //Debug.Log("m_Receive");
            //Debug.Log(m_ReceivePacket);
            //Debug.LogFormat($"StringlVariable = {m_ReceivePacket.m_StringlVariable}");
        }
    }

    void DoReceivePacket()
    {
        //Debug.LogFormat($"BoolVariable = {m_ReceivePacket.m_BoolVariable} " +
        //      $"IntlVariable = {m_ReceivePacket.m_IntVariable} " +
        //      $"m_IntArray[0] = {m_ReceivePacket.m_IntArray[0]} " +
        //      $"m_IntArray[1] = {m_ReceivePacket.m_IntArray[1] } " +
        //      $"FloatlVariable = {m_ReceivePacket.m_FloatlVariable} " +
        //      $"StringlVariable = {m_ReceivePacket.m_StringlVariable}");
        //출력: BoolVariable = True IntlVariable = 13 m_IntArray[0] = 7 m_IntArray[1] = 47 FloatlVariable = 2020 StringlVariable = Coder Zero
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

    void processJsonData(string _url)
    {
        Debug.Log("5");
        var jsonData = JsonUtility.FromJson<jsonClass.JsonClass>(_url);
        Debug.Log("6");
        Debug.Log(jsonData.items);
        if (jsonData.items != null)
        {
            for (int i = 0; i < jsonData.items.Count; i++)
            {
                posData[i] = new Vector3(jsonData.items[i].X, jsonData.items[i].Y, jsonData.items[i].Z);
                Debug.Log(posData[i].ToString("N5"));

            }
        }

    }
}