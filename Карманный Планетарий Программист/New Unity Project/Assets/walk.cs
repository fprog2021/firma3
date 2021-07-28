using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class walk : MonoBehaviour {


    public Vector3 w;
    public Vector3 s;
    public Vector3 a;
    public Vector3 d;
    public float walkForce = 2.0f;
    public bool isGrounded;
    Rigidbody rb;
    void Start()
    {
        rb = GetComponent<Rigidbody>();
        w = new Vector3(2.0f, 0.0f, 0.0f);
        s = new Vector3(-2.0f, 0.0f, 0.0f);
        d = new Vector3(0.0f, 0.0f, -2.0f);
        a = new Vector3(0.0f, 0.0f, 2.0f);
    }
    void OnCollisionStay()
    {
        isGrounded = true;
    }
    void Update()
    {
        if (Input.GetKey(KeyCode.W) && isGrounded)
        {
            rb.AddForce(w * walkForce, ForceMode.Impulse);
            isGrounded = false;
        }
        if (Input.GetKey(KeyCode.S) && isGrounded)
        {
            rb.AddForce(s * walkForce, ForceMode.Impulse);
            isGrounded = false;
        }
        if (Input.GetKey(KeyCode.A) && isGrounded)
        {
            rb.AddForce(a * walkForce, ForceMode.Impulse);
            isGrounded = false;
        }
        if (Input.GetKey(KeyCode.D) && isGrounded)
        {
            rb.AddForce(d * walkForce, ForceMode.Impulse);
            isGrounded = false;
        }
    }
}