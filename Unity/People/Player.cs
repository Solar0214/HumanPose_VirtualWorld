using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    //플레이어의 움직임 스피드, 수직, 수평 선언
    public float speed;
    float hAxis;
    float vAxis;
    bool wDown;
    //플레이어의 움직임 벡터값 변수 선언
    Vector3 moveVec;

    //플레이어의 움직임 애니메이션 변수 선언
    Animator anim;

    void Awake()
    {
        anim = GetComponentInChildren<Animator>();
    }

    void Update()
    {
        hAxis = Input.GetAxisRaw("Horizontal");
        vAxis = Input.GetAxisRaw("Vertical");
        //시프트키를 꾹 누르고 움직이면 달리게 설정
        wDown = Input.GetButton("Walk");

        //플레이어의 움직임 벡터값 설정
        moveVec = new Vector3(hAxis, 0, vAxis).normalized;

        //플레이어의 달리기 속도 0.3으로 설정(삼항연산자 사용할 경우)
        transform.position += moveVec * speed * (wDown ? 0.3f : 1f) * Time.deltaTime;

        //플레이어의 달리기 속도 0.3으로 설정(if문을 사용할 경우)
        //if(wDown)
        //    transform.position += moveVec * speed * 0.3f * Time.deltaTime;
        //else
        //    transform.position += moveVec * speed * Time.deltaTime;



        //플레이어의 달리기 벡터값 설정
        anim.SetBool("isRun", moveVec != Vector3.zero);
        anim.SetBool("isWalk", wDown);


        //플레이어의 회전값 설정(딱딱하게 움직임)
        //transform.LookAt(transform.position + moveVec);
        
        //플레이어의 회전값 설정(부드럽게 움직임)
        if (moveVec != Vector3.zero)
        {
            Vector3 relativePos = (transform.position + moveVec) - transform.position;
            Quaternion rotation = Quaternion.LookRotation(relativePos, Vector3.up);
            transform.rotation = Quaternion.Lerp(transform.rotation, rotation, Time.deltaTime * 10);
        }
    }
}
