import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel30FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel30FlatComponentChunk47

end RHP2Bridge
