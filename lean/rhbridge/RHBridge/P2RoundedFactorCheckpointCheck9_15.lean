import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk15 :
    P2RoundedFactorCheckpointData.panel9Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix60_eq :
    P2RoundedFactorCheckpointData.panel9Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk15.1

theorem panel9Prefix61_eq :
    P2RoundedFactorCheckpointData.panel9Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk15.2.1

theorem panel9Prefix62_eq :
    P2RoundedFactorCheckpointData.panel9Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk15.2.2.1

theorem panel9Prefix63_eq :
    P2RoundedFactorCheckpointData.panel9Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk15.2.2.2

end RHP2Bridge
