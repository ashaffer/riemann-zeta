import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel30FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel30FlatComponentChunk38

end RHP2Bridge
