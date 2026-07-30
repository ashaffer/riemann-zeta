import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel19FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel19FlatComponentChunk42

end RHP2Bridge
