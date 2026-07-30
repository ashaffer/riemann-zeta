import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel30FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel30FlatComponentChunk29

end RHP2Bridge
