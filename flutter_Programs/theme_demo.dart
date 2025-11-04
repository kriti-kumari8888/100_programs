import 'package:flutter/material.dart';

void main() => runApp(ThemeDemoApp());

class ThemeDemoApp extends StatefulWidget {
  @override
  _ThemeDemoAppState createState() => _ThemeDemoAppState();
}

class _ThemeDemoAppState extends State<ThemeDemoApp> {
  bool _dark = false;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Theme Demo',
      theme: _dark ? ThemeData.dark() : ThemeData.light(),
      home: Scaffold(
        appBar: AppBar(title: Text('Theme Demo')),
        body: Center(
          child: SwitchListTile(
            title: Text('Dark Mode'),
            value: _dark,
            onChanged: (v) => setState(() => _dark = v),
          ),
        ),
      ),
    );
  }
}
