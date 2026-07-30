import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk37 :
    P2RoundedFactorCheckpointData.panel19FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd13_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd13 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨13, by decide⟩ := by
  exact panel19FlatComponentChunk37

end RHP2Bridge
