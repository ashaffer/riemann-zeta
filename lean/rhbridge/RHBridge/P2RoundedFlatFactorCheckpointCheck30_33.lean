import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel30FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel30FlatComponentChunk33

end RHP2Bridge
