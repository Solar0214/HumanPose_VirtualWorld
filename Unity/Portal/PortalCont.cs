using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PortalCont : MonoBehaviour
{
    public Transform land1, land2;
    public Transform playerRoot, playerCam;
    public Transform portalCam;

    // Start is called before the first frame update
    void Start()
    {


    }

    // Update is called once per frame
    void Update()
    {

        //Vector3 playerOffset = playerCam.position - land1.position;

        //구한 오프셋을 랜드2의 포지션에 더하여 포털캠에 입힌다.
        //portalCam.position = portal.position + playerOffset;
    }

    //텔레포트 구현 클래스
    public void Teleport()
    {
        // land1과 land2를 바꿔준다.
        var playerLand = land1;
        land1 = land2;
        land2 = playerLand;

        //플레이어의 위치에 포털 카메라의 위치를 넣어준다.
        playerRoot.position = portalCam.position;
    }

}
