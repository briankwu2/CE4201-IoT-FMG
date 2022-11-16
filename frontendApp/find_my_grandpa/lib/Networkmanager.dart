import 'dart:io';

import 'package:http/http.dart' as http;
import 'dart:convert' as convert;

class NetowrkManager {
  static final NetowrkManager _netowrkManager = NetowrkManager._internal();
  static final String fmgURL = '127.0.0.1:5000';

  factory NetowrkManager() {
    return _netowrkManager;
  }

  NetowrkManager._internal();

  Future<dynamic> login(String username) async {
    // gets grandpa from database and

    // get grandpa and save it
    Map<String, String> parmsReq = {'grandpaID': username};
    print("Creating url");
    var url = Uri.http(fmgURL, "/grandpa_data/", parmsReq);

    print(url);
    try {
      var response = await http.get(url);
      print(response.statusCode);
      if (response.statusCode != 200) {
        return false;
      } else {
        var jsonDecoded =
            convert.jsonDecode(response.body) as Map<String, dynamic>;
        print(jsonDecoded);
        return jsonDecoded;
      }
    } catch (e) {
      print(e);
      return false;
    }
  }
}
