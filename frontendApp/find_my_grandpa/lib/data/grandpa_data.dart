import 'package:latlong2/latlong.dart';

import 'data_point.dart';
import 'dart:convert' as convert;

class GrandpaData {
  late String id;
  late List<DataPoint> history;
  GrandpaData() {
    // empty grandpa
    id = "";
    history = [];
  }
  GrandpaData.withJson(String jsonStr) {
    // parse json data into grandpa data
    var jsonData = convert.jsonDecode(jsonStr) as Map<String, dynamic>;
    print(jsonData);
    id = jsonData['grandpaID'];
    print(id);
    history = []; // initilize history
    final List<dynamic> hist = jsonData['history'];
    for (int i = 0; i < hist.length; i++) {
      // loop through hist and add to history in the datastructure
      history.add(DataPoint(hist[i]));
    }
  }

  LatLng firstPoint() {
    return history[0].point;
  }

  List<LatLng> getPosList() {
    List<LatLng> pList = [];
    for (int i = 0; i < history.length; i++) {
      pList.add(history[i].point);
    }
    return pList;
  }

  List<double> getBPM() {
    List<double> bpmList = [];
    for (int i = 0; i < history.length; i++) {
      bpmList.add(history[i].bpm + i);
    }
    return bpmList;
  }
}
