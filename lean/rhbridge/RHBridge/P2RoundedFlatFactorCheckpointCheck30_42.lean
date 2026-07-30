import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel30FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel30FlatComponentChunk42

end RHP2Bridge
