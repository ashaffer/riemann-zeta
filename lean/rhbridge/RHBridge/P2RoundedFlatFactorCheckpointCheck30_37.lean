import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel30FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel30FlatComponentChunk37

end RHP2Bridge
