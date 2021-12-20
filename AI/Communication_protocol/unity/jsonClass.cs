using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System.Text;

public class jsonClass : MonoBehaviour
{
    // Start is called before the first frame update
    [System.Serializable]
    public class JsonClass
    {
        public List<PoseList> items;

    }

    [System.Serializable]
    public class items
    {
        public string X;
        public string Y;
        public string Z;

    }

    [System.Serializable]
    public class PoseList
    {
        public float X;
        public float Y;
        public float Z;
    }
}
