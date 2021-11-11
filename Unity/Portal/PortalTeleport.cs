using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PortalTeleport : MonoBehaviour
{
    public PortalCont portalController;


    private void OnTriggerEnter(Collider other)
    {
        //충돌시 텔레포트를 해라
        portalController.Teleport();
    }
}
