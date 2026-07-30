import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel30FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel30FlatComponentChunk45

end RHP2Bridge
