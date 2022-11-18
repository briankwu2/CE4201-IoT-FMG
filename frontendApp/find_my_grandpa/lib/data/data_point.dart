import 'package:latlong2/latlong.dart';

class DataPoint {
  late int time;
  // late double lat;
  // late double log;
  late double bpm;
  late LatLng point;

  DataPoint(Map<String, dynamic> pointJson) {
    // parse json point into datastructure
    time = pointJson['time'];
    bpm = pointJson['bpm'];
    point = LatLng(pointJson['lat'].toDouble(), pointJson['log'].toDouble());
  }
}
