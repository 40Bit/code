//
//  Point.swift
//  Shapes
//

import UIKit

/// A point on the canvas that can be used (for example) to specify the center point of an object.
///
///   - `x` The horizontal (left/right) component of this point.
///   - `y` The vertical (up/down) component of this point.
/// - localizationKey: Point
public struct Point {
    
    /// The horizontal (left/right) component of this point.
    /// - localizationKey: Point.x
    public var x = 0.0
    
    /// The vertical (up/down) component of this point.
    /// - localizationKey: Point.y
    public var y = 0.0
    
    internal var cgPoint: CGPoint {
        return CGPoint(x: CGFloat(x), y: CGFloat(y))
    }
    
    /// Creates a Point with the given x and y.
    ///
    /// `x` The horizontal (left/right) component of this point.
    /// `y` The vertical (up/down) component of this point.
    /// - localizationKey: Point(x:y:)
    public init(x:Double, y: Double) {
        self.x = x
        self.y = y
    }
        
    internal init(_ cgPoint: CGPoint) {
        x = Double(cgPoint.x)
        y = Double(cgPoint.y)
    }
    
}

extension Point: CustomPlaygroundDisplayConvertible {
    public var playgroundDescription: Any {
        get {
            return "x = \(x), y = \(y)"
        }
    }
}

