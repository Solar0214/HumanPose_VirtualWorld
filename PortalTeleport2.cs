using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PortalTeleport2 : MonoBehaviour
{
    public PortalCont2 portalController2;


    private void OnTriggerEnter(Collider other)
    {
        //충돌시 텔레포트를 해라
        portalController2.Teleport();
    }
}
