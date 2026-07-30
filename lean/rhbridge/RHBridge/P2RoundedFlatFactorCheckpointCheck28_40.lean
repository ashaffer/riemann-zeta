import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk40 :
    P2RoundedFactorCheckpointData.panel28FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd16_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd16 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨16, by decide⟩ := by
  exact panel28FlatComponentChunk40

end RHP2Bridge
