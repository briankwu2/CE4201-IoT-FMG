import 'dart:io';

import 'package:find_my_grandpa/Networkmanager.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';

class LoinPage extends StatefulWidget {
  const LoinPage({Key? key}) : super(key: key);

  @override
  State<LoinPage> createState() => _LoinPageState();
}

class _LoinPageState extends State<LoinPage> {
  final myController = TextEditingController();

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    myController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Login"),
        ),
        body: Container(
            color: Colors.white,
            child: Center(
              child: Column(
                children: [
                  Text("Login"),
                  Container(
                    child: Text(""),
                    height: 50,
                  ),
                  Row(
                    children: [
                      Expanded(child: Container()),
                      Expanded(
                          child: Container(
                        child: TextField(
                            controller: myController,
                            decoration: InputDecoration(
                                border: OutlineInputBorder(),
                                labelText: 'Username')),
                      )),
                      Expanded(child: Container())
                    ],
                  ),
                  Container(
                    child: Text(""),
                    height: 50,
                  ),
                  ElevatedButton(
                      onPressed: () {
                        print(myController.text);
                        NetowrkManager().login(myController.text);
                      },
                      child: Text("login"))
                ],
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
              ),
            )));
  }
}
