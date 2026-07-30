import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel30FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel30FlatComponentChunk34

end RHP2Bridge
