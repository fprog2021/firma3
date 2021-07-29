using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Test : MonoBehaviour {

    public Rigidbody rb;
    public float force;
    // Use this for initialization
	void Start () {
        rb = GetComponent<Rigidbody>();
	}
	
	// Update is called once per frame
	void Update () {
		
	}

    public void OnDown()
    {
        rb.AddForce(Vector3.up*force, ForceMode.Impulse);
    }
}