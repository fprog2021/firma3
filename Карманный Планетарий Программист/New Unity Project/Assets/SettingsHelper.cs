using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class SettingsHelper : MonoBehaviour{

    public UnityEngine.UI.Button stylization;
    public UnityEngine.UI.Button exitbutton;
    public UnityEngine.UI.Button Themebutton;
    public UnityEngine.UI.Button Buttontheme;

    void Start() { 
    {
        stylization.onClick.AddListener(Stylization);
        exitbutton.onClick.AddListener(Exit);
        Themebutton.onClick.AddListener(Theme);
        Buttontheme.onClick.AddListener(ButtonTheme);
    }

        void Exit()
        {
            SceneManager.LoadScene("MainMenu");
        }

        void Stylization()
        {
            SceneManager.LoadScene("Settings2");
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
