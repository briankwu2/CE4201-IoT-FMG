import 'dart:io';

import 'package:find_my_grandpa/support_classes/network_manager.dart';
import 'package:find_my_grandpa/views/dashboard_widget.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';

class LoinPage extends StatefulWidget {
  static const String route = "/login";
  const LoinPage({Key? key}) : super(key: key);

  @override
  State<LoinPage> createState() => _LoinPageState();
}

class _LoinPageState extends State<LoinPage> {
  final myController = TextEditingController();

  bool loginFaild = false;

  @override
  void dispose() {
    // Clean up the controller when the widget is disposed.
    myController.dispose();
    super.dispose();
  }

  // Widget buildLoginFeild() {
  //   if (startedLogin) {}
  //   return FutureBuilder<bool>(
  //       future: isLoggedIn, // a previously-obtained Future<String> or null
  //       builder: (BuildContext context, AsyncSnapshot<bool> snapshot) {
  //         if (snapshot.hasData) {
  //           if (snapshot.data == true) {
  //             // logged in successfully
  //             //Navigator.push(context, route)
  //           } else {
  //             // did not log in successfully
  //           }
  //         } else {
  //           return TextField(
  //               controller: myController,
  //               decoration: InputDecoration(
  //                   border: OutlineInputBorder(), labelText: 'Username'));
  //         }
  //       });
  // }
  void loginFunc(BuildContext context) async {
    bool success = await NetowrkManager().login(myController.text);
    if (success) {
      // able to login
      Navigator.pushNamed(context, DashBoardWidget.route);
      // Navigator.push(
      //     context, MaterialPageRoute(builder: (context) => DashBoardWidget()));
    } else {
      // unsuccessfull
      setState(() {
        loginFaild = true;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        // appBar: AppBar(
        //   title: Text("Login"),
        // ),
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
                        loginFunc(context);
                      },
                      child: Text("login"))
                ],
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.center,
              ),
            )));
  }
}
