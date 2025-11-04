import 'package:flutter/material.dart';

void main() => runApp(DrawerDemo());

class DrawerDemo extends StatelessWidget {
  @override
  Widget build(BuildContext context) => MaterialApp(home: HomeWithDrawer());
}

class HomeWithDrawer extends StatelessWidget {
  @override
  Widget build(BuildContext context) => Scaffold(
        appBar: AppBar(title: Text('Drawer Demo')),
        drawer: Drawer(
          child: ListView(
            padding: EdgeInsets.zero,
            children: [
              DrawerHeader(
                decoration: BoxDecoration(color: Colors.blue),
                child: Text('Menu', style: TextStyle(color: Colors.white, fontSize: 24)),
              ),
              ListTile(leading: Icon(Icons.home), title: Text('Home')),
              ListTile(leading: Icon(Icons.settings), title: Text('Settings')),
            ],
          ),
        ),
        body: Center(child: Text('Open the drawer from the left')),
      );
}
