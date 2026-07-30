import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk15 :
    P2RoundedFactorCheckpointData.panel4Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix60_eq :
    P2RoundedFactorCheckpointData.panel4Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk15.1

theorem panel4Prefix61_eq :
    P2RoundedFactorCheckpointData.panel4Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk15.2.1

theorem panel4Prefix62_eq :
    P2RoundedFactorCheckpointData.panel4Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk15.2.2.1

theorem panel4Prefix63_eq :
    P2RoundedFactorCheckpointData.panel4Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk15.2.2.2

end RHP2Bridge
