using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MainmenuHelper : MonoBehaviour {

	public UnityEngine.UI.Button startbutton;
	public UnityEngine.UI.Button exitbutton;
	public UnityEngine.UI.Button Instruction;
	public UnityEngine.UI.Button settings;

	// Use this for initialization
	void Start () {
		startbutton.onClick.AddListener(ToPlanets);
		exitbutton.onClick.AddListener(ExitGame);
		Instruction.onClick.AddListener(instruction);
		settings.onClick.AddListener(Settings);
		Cursor.lockState = CursorLockMode.None;
		Cursor.visible = true;
	}
	
	void ToPlanets () {
		SceneManager.LoadScene("Planets");
	}

	void ExitGame()
	{
		Application.Quit();
	}

	void instruction()
    {
		SceneManager.LoadScene("Instruction");
    }

	void Settings()
    {
		SceneManager.LoadScene("Settings");
    }
}
