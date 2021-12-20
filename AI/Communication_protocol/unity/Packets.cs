using System;
using System.Runtime.InteropServices;

[StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
[Serializable]
public struct Packet
{
    [MarshalAs(UnmanagedType.Bool)]
    public bool m_BoolVariable;
    public int m_IntVariable;
    [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
    public int[] m_IntArray;
    public float m_FloatlVariable;
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 64)]
    public string m_StringlVariable;
}
