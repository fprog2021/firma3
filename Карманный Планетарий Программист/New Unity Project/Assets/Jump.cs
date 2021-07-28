using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class Jump : MonoBehaviour {

    public GameObject cube;
    public float jumpForce = 3f;
    bool isGrounded = true;
    private Rigidbody rb;
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }
    void OnCollisionStay()
    {
        isGrounded = true;
    }
    void Update()
    {
        RaycastHit ray;
        if ((Input.GetKeyDown(KeyCode.Space) && isGrounded) && Physics.Raycast(transform.position, Vector3.down, out ray, .6f)&& ray.collider.CompareTag("Terrain")){

            rb.AddForce(Vector3.up * jumpForce, ForceMode.Impulse);
            isGrounded = false;
        }
        rb.AddForce(Vector3.forward * (Input.GetAxis("Vertical")*1f), ForceMode.Impulse);
        rb.AddForce(Vector3.left * (Input.GetAxis("Horizontal") * 1f), ForceMode.Impulse);
    }
}
