using System.Collections;
using System;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class CollisionDelete : MonoBehaviour {

    public Text Schet ;
    //Переменная отвечающая за текст
    int a = 0;
    //Создаётся переменная,отвечающая за игровые очки
    private void OnCollisionEnter(Collision collision)
    {
        if (collision.collider.CompareTag("Player"))
        {
            a++;
            //К переменной ,отвечающей за игровые очки,засчитывается гол
            Destroy(this.gameObject);
            //Уничтожается объект ,на который наложен скрипт
            Schet.text = Convert.ToString(a);
            //В переменную ,отвечающую за текст записывается содержимое перемменой,отвечающей за игровые очки
        }
    }
}
