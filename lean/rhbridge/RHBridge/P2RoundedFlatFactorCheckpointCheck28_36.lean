import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel28FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel28FlatComponentChunk36

end RHP2Bridge
