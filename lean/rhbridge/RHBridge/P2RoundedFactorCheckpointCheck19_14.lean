import RHBridge.P2RoundedFactorCheckpointData19

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FactorChunk14 :
    P2RoundedFactorCheckpointData.panel19Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨19, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel19Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨19, by decide⟩ := by
  decide +kernel

theorem panel19Prefix56_eq :
    P2RoundedFactorCheckpointData.panel19Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk14.1

theorem panel19Prefix57_eq :
    P2RoundedFactorCheckpointData.panel19Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk14.2.1

theorem panel19Prefix58_eq :
    P2RoundedFactorCheckpointData.panel19Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk14.2.2.1

theorem panel19Prefix59_eq :
    P2RoundedFactorCheckpointData.panel19Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨19, by decide⟩ := by
  exact panel19FactorChunk14.2.2.2

end RHP2Bridge
