import 'dart:io';

import 'package:http/http.dart' as http;
import 'dart:convert' as convert;

class NetowrkManager {
  static final NetowrkManager _netowrkManager = NetowrkManager._internal();
  static final String fmgURL = "127.0.0.1:5000";

  factory NetowrkManager() {
    return _netowrkManager;
  }

  NetowrkManager._internal();

  void login(String username) async {
    // gets grandpa from database and

    // get grandpa and save it
    Map<String, dynamic> parmsReq = {'grandpaID': username};
    var url = Uri.http(fmgURL, "/grandpa_data/", parmsReq);
    var response = await http.get(url);
    if (response.statusCode == 200) {
      // print(response.statusCode);
      print("response successful");
      // var jsonResponse = convert.jsonDecode(response.body) as Map<String, dynamic>;
      // print(jsonResponse.toString());
    } else {
      print('Request failed with status: ${response.statusCode}.');
    }
  }
}
