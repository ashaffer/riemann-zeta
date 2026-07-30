import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel30FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel30FlatComponentChunk31

end RHP2Bridge
