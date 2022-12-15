import 'dart:io';

import 'package:find_my_grandpa/data/grandpa_data.dart';
import 'package:find_my_grandpa/support_classes/state_manager.dart';
import 'package:http/http.dart' as http;
import 'dart:convert' as convert;

class NetowrkManager {
  static final NetowrkManager _netowrkManager = NetowrkManager._internal();
  static final String fmgURL =
      'ec2-3-20-227-73.us-east-2.compute.amazonaws.com'; //'127.0.0.1:5000';

  factory NetowrkManager() {
    return _netowrkManager;
  }

  NetowrkManager._internal();

  Future<bool> login(String username, String password) async {
    // true if login successful
    // false if login unsuccesful

    // gets grandpa from database and
    // get grandpa and save it
    Map<String, String> parmsReq = {
      'grandpaID': username,
      'password': password
    };
    print("Creating url");
    var url = Uri.http(fmgURL, "/grandpa_data/", parmsReq);

    print(url);
    try {
      var response = await http.get(url);
      print(response.statusCode);
      if (response.statusCode != 200) {
        return false;
      } else {
        // decodes json code and sends it to the constructor class
        // Map<String, dynamic> jsonDecoded = Map.castFrom(
        //     convert.jsonDecode(response.body) as Map<String, dynamic>);
        //var jsonDecoded = convert.jsonDecode(response.body);
        print(response.body);
        GrandpaData gData = GrandpaData.withJson(response.body);
        print("Created grandpa successfully");
        print(gData.id);
        // sets the grandpa data to the state manager
        StateManager().setGrandpaData(gData);
        return true;
      }
    } catch (e) {
      print(e);
      return false;
    }
  }
}
