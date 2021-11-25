using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Follow1 : MonoBehaviour
{
    public float fbspeed = 5.0f; //카메라의 상하 회전 속도 변수 선언
    public float rotspeed = 3.0f; //카메라의 좌우 회전 속도 변수 선언
    public Camera fpsCam;
    //Vector3 fb = new Vector3(0, 0, 1); //Z축으로 1만큼 이동한 3차원 좌표값
    //Vector3 lr = new Vector3(0, 1, 0); //Y축으로 1만큼 이동한 3차원 좌표값

    void Start()
    {
        
    }

    void Update()
    {
        MoveCtrl ();
        RotCtrl ();
        //float v = Input.GetAxis("Vertical") * Time.deltaTime; //눌린 키보드의 방향키 확인, 프레임 간격의 시간
        //float h = Input.GetAxis("Horizontal") * Time.deltaTime; //프레임 주사율에 관계없이 일정하게 움직이도록 설정
        //transform.Translate(fb * v * fbspeed); //이동 메서드 변수
        //transform.Rotate(lr * h * lrspeed); //회전 메서드 변수
        
    }
    void MoveCtrl()
    {
        if (Input.GetKeyDown(KeyCode.W))
        {
            this.transform.Translate(Vector3.forward * fbspeed * Time.deltaTime);
        }
        if (Input.GetKeyDown(KeyCode.S))
        {
            this.transform.Translate(Vector3.back * fbspeed * Time.deltaTime);
        }
        if (Input.GetKeyDown(KeyCode.A))
        {
            this.transform.Translate(Vector3.left * fbspeed * Time.deltaTime);
        }
        if (Input.GetKeyDown(KeyCode.D))
        {
            this.transform.Translate(Vector3.right * fbspeed * Time.deltaTime);
        }
    }
    void RotCtrl()
    {
        float rotx = Input.GetAxis("Mouse Y") * rotspeed; //X축에 속도를 곱해 조절 함
        float roty = Input.GetAxis("Mouse X") * rotspeed; //Y축에 속도를 곱해 조절 함

        this.transform.localRotation *= Quaternion.Euler(0, roty, 0); //스크립트가 적용된 오브젝트안에 로컬축 갱신
        fpsCam.transform.localRotation *= Quaternion.Euler(-rotx, 0, 0); //적용된 카메라를 -X축으로 갱신
    }
}
