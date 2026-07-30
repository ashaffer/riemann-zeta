import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel30FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel30FlatComponentChunk27

end RHP2Bridge
