import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk15 :
    P2RoundedFactorCheckpointData.panel0Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix60_eq :
    P2RoundedFactorCheckpointData.panel0Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk15.1

theorem panel0Prefix61_eq :
    P2RoundedFactorCheckpointData.panel0Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk15.2.1

theorem panel0Prefix62_eq :
    P2RoundedFactorCheckpointData.panel0Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk15.2.2.1

theorem panel0Prefix63_eq :
    P2RoundedFactorCheckpointData.panel0Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk15.2.2.2

end RHP2Bridge
