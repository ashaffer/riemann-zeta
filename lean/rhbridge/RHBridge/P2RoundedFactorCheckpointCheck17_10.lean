import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk10 :
    P2RoundedFactorCheckpointData.panel17Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix40_eq :
    P2RoundedFactorCheckpointData.panel17Prefix40 =
      normalizedPrefixTermAtomApprox ⟨40, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk10.1

theorem panel17Prefix41_eq :
    P2RoundedFactorCheckpointData.panel17Prefix41 =
      normalizedPrefixTermAtomApprox ⟨41, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk10.2.1

theorem panel17Prefix42_eq :
    P2RoundedFactorCheckpointData.panel17Prefix42 =
      normalizedPrefixTermAtomApprox ⟨42, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk10.2.2.1

theorem panel17Prefix43_eq :
    P2RoundedFactorCheckpointData.panel17Prefix43 =
      normalizedPrefixTermAtomApprox ⟨43, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk10.2.2.2

end RHP2Bridge
