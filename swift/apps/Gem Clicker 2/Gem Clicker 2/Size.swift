//
//  Size.swift
//  Shapes
//

import UIKit

/// A size on the canvas.
///
///  `width` The width component of this size.
///  `height` The height component of this size.
/// - localizationKey: Size
public struct Size {
    
    /// The width component of this size.
    /// - localizationKey: Size.width
    public var width = 0.0
    
    /// The height component of this size.
    /// - localizationKey: Size.height
    public var height = 0.0
    
    internal var cgSize: CGSize {
        return CGSize(width: CGFloat(width), height: CGFloat(height))
    }
    
    /// Creates a Size with the given width and height.
    ///
    /// `width` The width component of this size.
    /// `height` The height component of this size.
    /// - localizationKey: Size(width:height:)
    public init(width: Double, height: Double) {
        self.width = width
        self.height = height
    }
    
    internal init(_ cgSize: CGSize) {
        self.width = Double(cgSize.width)
        self.height = Double(cgSize.height)
    }
    
}

extension Size: CustomPlaygroundDisplayConvertible {
    public var playgroundDescription: Any {
        get {
            return "Width = \(width), height = \(height)"
        }
    }
}
