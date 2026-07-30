import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel30FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel30FlatComponentChunk39

end RHP2Bridge
