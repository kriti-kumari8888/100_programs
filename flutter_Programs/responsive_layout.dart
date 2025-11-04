import 'package:flutter/material.dart';

void main() => runApp(ResponsiveLayoutDemo());

class ResponsiveLayoutDemo extends StatelessWidget {
  @override
  Widget build(BuildContext context) => MaterialApp(home: ResponsiveHome());
}

class ResponsiveHome extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Responsive Layout')),
      body: LayoutBuilder(
        builder: (context, constraints) {
          if (constraints.maxWidth < 600) {
            // phone
            return ListView(
              children: List.generate(6, (i) => Card(child: ListTile(title: Text('Item \\${i + 1}')))),
            );
          } else {
            // tablet/desktop: grid
            return GridView.count(
              crossAxisCount: 3,
              children: List.generate(6, (i) => Card(child: Center(child: Text('Item \\${i + 1}')))),
            );
          }
        },
      ),
    );
  }
}
