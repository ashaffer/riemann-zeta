import RHBridge.P2RoundedFlatFactorCheckpointData30

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel30FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel30FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel30FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel30TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel30FlatComponentChunk41

end RHP2Bridge
