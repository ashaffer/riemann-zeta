import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel19FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel19FlatComponentChunk43

end RHP2Bridge
