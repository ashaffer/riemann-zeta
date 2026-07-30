import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel18FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel18FlatComponentChunk41

end RHP2Bridge
